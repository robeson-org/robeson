import { defineCollection } from "astro:content";
import { z } from "astro/zod";
import { glob } from "astro/loaders";
const publications = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content" }),
  schema: z.object({
    title: z.string(),
    revised: z.string().optional(),
    description: z.string(),
    status: z.enum(["placeholder", "draft", "published"]),
    order: z.number(),
    version: z.string().optional(),
    group: z.enum(["standard", "notes", "sources", "overview"]).optional(),
    sourcePath: z.string().optional(),
    bodyTitle: z.boolean().default(false),
    featured: z.boolean().default(true),
    navTitle: z.string().optional(),
  }),
});
export const collections = { publications };
