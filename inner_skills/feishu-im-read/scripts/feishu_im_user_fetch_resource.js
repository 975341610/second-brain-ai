import { promises as fs } from "node:fs";
import { dirname, join } from "node:path";
import { tmpdir } from "node:os";
import { runCli } from "./internal/_cli.js";

const MIME_TO_EXT = {
  "image/png": ".png",
  "image/jpeg": ".jpg",
  "image/jpg": ".jpg",
  "image/gif": ".gif",
  "image/webp": ".webp",
  "image/svg+xml": ".svg",
  "image/bmp": ".bmp",
  "image/tiff": ".tiff",
  "video/mp4": ".mp4",
  "video/mpeg": ".mpeg",
  "video/quicktime": ".mov",
  "video/x-msvideo": ".avi",
  "video/webm": ".webm",
  "audio/mpeg": ".mp3",
  "audio/wav": ".wav",
  "audio/ogg": ".ogg",
  "audio/mp4": ".m4a",
  "application/pdf": ".pdf",
  "application/zip": ".zip",
  "text/plain": ".txt",
  "application/json": ".json",
};

async function streamToBuffer(stream) {
  const chunks = [];
  for await (const chunk of stream) {
    chunks.push(Buffer.isBuffer(chunk) ? chunk : Buffer.from(chunk));
  }
  return Buffer.concat(chunks);
}

function guessExt(contentType) {
  if (!contentType) return "";
  const mime = String(contentType).split(";")[0].trim();
  return MIME_TO_EXT[mime] ?? "";
}

await runCli(async ({ sdk, opts, input }) => {
  sdk.authReason = "下载消息中的文件或图片";
  const p = input ?? {};
  if (!p.message_id) throw new Error("missing message_id");
  if (!p.file_key) throw new Error("missing file_key");
  if (p.type !== "image" && p.type !== "file") throw new Error("type must be image|file");

  const res = await sdk.im.v1.messageResource.get(
      { params: { type: p.type }, path: { message_id: p.message_id, file_key: p.file_key } },
      opts,
  );

  const headerCT =
      res?.headers?.["content-type"] ||
      res?.headers?.["Content-Type"] ||
      "";

  // 先提取 buffer 和真实 contentType，再算扩展名
  let buffer;
  let contentType = headerCT;

  // 代理返回模式：Go 侧将文件内容 base64 编码后放在 data.file_base64
  const proxyData = res?.data ?? res;
  if (proxyData?.file_base64) {
    buffer = Buffer.from(proxyData.file_base64, "base64");
    contentType = proxyData.content_type || headerCT;
  } else if (typeof res.getReadableStream === "function") {
    buffer = await streamToBuffer(res.getReadableStream());
  } else if (res?.data instanceof ArrayBuffer) {
    buffer = Buffer.from(res.data);
  } else if (Buffer.isBuffer(res?.data)) {
    buffer = res.data;
  } else if (res?.data && typeof res.data.pipe === "function") {
    buffer = await streamToBuffer(res.data);
  } else {
    throw new Error("unsupported response type for resource download");
  }

  const ext = guessExt(contentType);
  const savedPath = `feishu-im-resource/${p.type}/${p.file_key}${ext}`;
  const outputPath = join(tmpdir(), savedPath);

  await fs.mkdir(dirname(outputPath), { recursive: true });
  await fs.writeFile(outputPath, buffer);

  return {
    message_id: p.message_id,
    file_key: p.file_key,
    type: p.type,
    content_type: contentType,
    size_bytes: buffer.length,
    saved_path: savedPath,
  };
});

