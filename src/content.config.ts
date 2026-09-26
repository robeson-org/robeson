import { defineCollection } from "astro:content";
import { z } from "astro/zod";
import { glob } from "astro/loaders";
const publications = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content" }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    status: z.enum(["placeholder", "draft", "published"]),
    order: z.number(),
    version: z.string().optional(),
  }),
});
export const collections = { publications };
