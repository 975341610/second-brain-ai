const fs = require('fs');
function loadTyporaTheme(cssString, themeName) {
  const scope = `.typora-wrapper[data-theme="${themeName}"]`;
  let processed = cssString.replace(/\/\*[\s\S]*?\*\//g, '');
  const transformSelectorLine = (selectors) => {
    return selectors.split(',')
      .map(s => s.trim())
      .filter(s => s.length > 0)
      .map(s => {
        if (s === 'body' || s === 'html' || s === ':root') return scope;
        if (s.startsWith('body ') || s.startsWith('html ') || s.startsWith(':root ')) {
          return s.replace(/^(body|html|:root)/, scope);
        }
        return `${scope} ${s}`;
      })
      .join(', ');
  };
  return processed.replace(/([^{}]+)\{/g, (match, selectorPart, offset) => {
    const trimmedSelector = selectorPart.trim();
    if (trimmedSelector.startsWith('@')) return match;
    return transformSelectorLine(selectorPart) + ' {';
  });
}
const css = fs.readFileSync('second-brain-ai/frontend/public/themes/vue.css', 'utf-8');
const result = loadTyporaTheme(css, 'typora-vue');
fs.writeFileSync('test_out.css', result);
console.log(result.substring(0, 500));
