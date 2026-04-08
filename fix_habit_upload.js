const fs = require('fs');
const file = '/workspace/iris_4313d091-e484-4384-8564-8ce91e478bc4/nova_repo/nova-block/src/components/widgets/HabitTrackerComponent.tsx';
let code = fs.readFileSync(file, 'utf8');

const additionalFunctions = `
const fileToDataUrl = (file: File): Promise<string> => {
  return new Promise((resolve, reject) => {
    const reader = new FileReader();
    reader.onload = (e) => resolve(e.target?.result as string);
    reader.onerror = reject;
    reader.readAsDataURL(file);
  });
};

const fileToCompressedDataUrl = async (file: File, maxSize = 128, quality = 0.82) => {
  const dataUrl = await fileToDataUrl(file);
  if (!dataUrl.startsWith('data:image/')) return dataUrl;

  const img = new Image();
  await new Promise<void>((resolve, reject) => {
    img.onload = () => resolve();
    img.onerror = () => reject(new Error('image load failed'));
    img.src = dataUrl;
  });

  const scale = Math.min(1, maxSize / Math.max(img.width, img.height));
  const width = Math.max(1, Math.round(img.width * scale));
  const height = Math.max(1, Math.round(img.height * scale));

  const canvas = document.createElement('canvas');
  canvas.width = width;
  canvas.height = height;

  const ctx = canvas.getContext('2d');
  ctx?.drawImage(img, 0, 0, width, height);

  return canvas.toDataURL('image/webp', quality);
};
`;

code = code.replace(
  "const uploadFileToLocal = async (file: File): Promise<string> => {", 
  additionalFunctions + "\nconst uploadFileToLocal = async (file: File): Promise<string> => {"
);

const uploadCodeOld = `<input type="file" className="hidden" onChange={async (e) => {
                            const f = e.target.files?.[0];
                            if(f) updateHabit(h.id, { icon: await uploadFileToLocal(f) });
                          }} />`;

const uploadCodeNew = `<input type="file" className="hidden" accept="image/*" onChange={async (e) => {
                            const f = e.target.files?.[0];
                            if(f) {
                              try {
                                const url = await uploadFileToLocal(f);
                                updateHabit(h.id, { icon: url });
                              } catch (err) {
                                console.warn('Physical upload failed, fallback to base64:', err);
                                try {
                                  const base64 = await fileToCompressedDataUrl(f, 128, 0.8);
                                  updateHabit(h.id, { icon: base64 });
                                } catch (e) {
                                  console.error(e);
                                }
                              }
                            }
                          }} />`;

code = code.replace(uploadCodeOld, uploadCodeNew);

fs.writeFileSync(file, code);
