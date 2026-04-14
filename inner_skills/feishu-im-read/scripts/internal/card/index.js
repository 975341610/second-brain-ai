/**
 * Copyright (c) 2026 ByteDance Ltd. and/or its affiliates
 * SPDX-License-Identifier: MIT
 *
 * Entry point for the interactive (card) message converter.
 */
import { safeParse } from './utils.js';
import { CardConverter, MODE } from './card-converter.js';
import { convertLegacyCard } from './legacy.js';
export const convertInteractive = (raw) => {
    const parsed = safeParse(raw);
    if (!parsed) {
        return { content: '[interactive card]', resources: [] };
    }
    if (typeof parsed.json_card === 'string') {
        const converter = new CardConverter(MODE.Concise);
        const result = converter.convert(parsed);
        return { content: result.content || '[interactive card]', resources: [] };
    }
    return convertLegacyCard(parsed);
};
