import { test, expect } from '@playwright/test';
test('operations console renders', async ({page}) => { await page.goto('/'); await expect(page.getByRole('heading',{name:'Operations Console'})).toBeVisible(); });
