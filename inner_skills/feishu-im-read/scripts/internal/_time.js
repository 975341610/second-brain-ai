const BJ_OFFSET_MS = 8 * 60 * 60 * 1000;

function formatBeijingISO(d) {
  const bj = new Date(d.getTime() + BJ_OFFSET_MS);
  const y = bj.getUTCFullYear();
  const mo = String(bj.getUTCMonth() + 1).padStart(2, "0");
  const da = String(bj.getUTCDate()).padStart(2, "0");
  const h = String(bj.getUTCHours()).padStart(2, "0");
  const mi = String(bj.getUTCMinutes()).padStart(2, "0");
  const s = String(bj.getUTCSeconds()).padStart(2, "0");
  return `${y}-${mo}-${da}T${h}:${mi}:${s}+08:00`;
}

export function dateTimeToSecondsString(datetime) {
  const d = new Date(datetime);
  if (Number.isNaN(d.getTime())) {
    throw new Error(
      `无法解析 ISO 8601 时间: "${datetime}"。格式示例: 2026-02-27T14:30:00+08:00`,
    );
  }
  return Math.floor(d.getTime() / 1000).toString();
}

function toBeijingDate(d) {
  return new Date(d.getTime() + BJ_OFFSET_MS);
}

function beijingStartOfDay(bjDate) {
  return new Date(
    Date.UTC(bjDate.getUTCFullYear(), bjDate.getUTCMonth(), bjDate.getUTCDate()) -
      BJ_OFFSET_MS,
  );
}

function beijingEndOfDay(bjDate) {
  return new Date(
    Date.UTC(
      bjDate.getUTCFullYear(),
      bjDate.getUTCMonth(),
      bjDate.getUTCDate(),
      23,
      59,
      59,
    ) - BJ_OFFSET_MS,
  );
}

function subtractFromNow(now, n, unit) {
  const d = new Date(now);
  if (unit === "minute") d.setMinutes(d.getMinutes() - n);
  else if (unit === "hour") d.setHours(d.getHours() - n);
  else if (unit === "day") d.setDate(d.getDate() - n);
  else throw new Error(`不支持的时间单位: ${unit}`);
  return d;
}

export function parseTimeRangeToSeconds(input) {
  const now = new Date();
  const bjNow = toBeijingDate(now);
  let start;
  let end;
  switch (input) {
    case "today":
      start = beijingStartOfDay(bjNow);
      end = now;
      break;
    case "yesterday": {
      const d = new Date(bjNow);
      d.setUTCDate(d.getUTCDate() - 1);
      start = beijingStartOfDay(d);
      end = beijingEndOfDay(d);
      break;
    }
    case "day_before_yesterday": {
      const d = new Date(bjNow);
      d.setUTCDate(d.getUTCDate() - 2);
      start = beijingStartOfDay(d);
      end = beijingEndOfDay(d);
      break;
    }
    case "this_week": {
      const day = bjNow.getUTCDay();
      const diffToMon = day === 0 ? 6 : day - 1;
      const monday = new Date(bjNow);
      monday.setUTCDate(monday.getUTCDate() - diffToMon);
      start = beijingStartOfDay(monday);
      end = now;
      break;
    }
    case "last_week": {
      const day = bjNow.getUTCDay();
      const diffToMon = day === 0 ? 6 : day - 1;
      const thisMonday = new Date(bjNow);
      thisMonday.setUTCDate(thisMonday.getUTCDate() - diffToMon);
      const lastMonday = new Date(thisMonday);
      lastMonday.setUTCDate(lastMonday.getUTCDate() - 7);
      const lastSunday = new Date(thisMonday);
      lastSunday.setUTCDate(lastSunday.getUTCDate() - 1);
      start = beijingStartOfDay(lastMonday);
      end = beijingEndOfDay(lastSunday);
      break;
    }
    case "this_month": {
      const firstDay = new Date(
        Date.UTC(bjNow.getUTCFullYear(), bjNow.getUTCMonth(), 1),
      );
      start = beijingStartOfDay(firstDay);
      end = now;
      break;
    }
    case "last_month": {
      const firstDayThisMonth = new Date(
        Date.UTC(bjNow.getUTCFullYear(), bjNow.getUTCMonth(), 1),
      );
      const lastDayPrevMonth = new Date(firstDayThisMonth);
      lastDayPrevMonth.setUTCDate(lastDayPrevMonth.getUTCDate() - 1);
      const firstDayPrevMonth = new Date(
        Date.UTC(
          lastDayPrevMonth.getUTCFullYear(),
          lastDayPrevMonth.getUTCMonth(),
          1,
        ),
      );
      start = beijingStartOfDay(firstDayPrevMonth);
      end = beijingEndOfDay(lastDayPrevMonth);
      break;
    }
    default: {
      const m = String(input).match(/^last_(\d+)_(minutes?|hours?|days?)$/);
      if (!m) {
        throw new Error(
          `不支持的 relative_time 格式: "${input}"。支持: today, yesterday, day_before_yesterday, this_week, last_week, this_month, last_month, last_{N}_{unit}（unit: minutes/hours/days）`,
        );
      }
      const n = Number.parseInt(m[1], 10);
      const unit = m[2].replace(/s$/, "");
      start = subtractFromNow(now, n, unit);
      end = now;
      break;
    }
  }
  return {
    start: dateTimeToSecondsString(formatBeijingISO(start)),
    end: dateTimeToSecondsString(formatBeijingISO(end)),
  };
}

