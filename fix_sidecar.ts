import * as fs from 'fs';

const sidecarPath = 'clean_repo/src/main/sidecar.ts';
let code = fs.readFileSync(sidecarPath, 'utf-8');

// Add PYTHONUNBUFFERED
code = code.replace(/HOST: '127.0.0.1'/g, "HOST: '127.0.0.1',\n        PYTHONUNBUFFERED: '1'");

// Add timeout to fetch
const fetchReplacement = `
        const controller = new AbortController();
        const timeoutId = setTimeout(() => controller.abort(), 2000);
        const response = await fetch(healthUrl, { signal: controller.signal as any });
        clearTimeout(timeoutId);
`;
code = code.replace(/const response = await fetch\(healthUrl\);/, fetchReplacement);

// Add error log to the promise
code = code.replace(/this\.process\?\.on\('error', \(err\) => \{/, `this.process?.on('error', (err) => {\n        log.error('Backend process emitted error event:', err);`);

// Quote command if using shell: true (but we use shell: false, which is fine)
// We will explicitly ensure we catch any synchronous error
code = code.replace(/this\.process = spawn\(/, `try {\n      this.process = spawn(`);
code = code.replace(/    if \(this\.process\.stdout\) \{/, `    } catch (err) {\n      log.error('Synchronous error during spawn:', err);\n      throw err;\n    }\n\n    if (this.process.stdout) {`);

fs.writeFileSync(sidecarPath, code, 'utf-8');
console.log('Fixed sidecar.ts');
