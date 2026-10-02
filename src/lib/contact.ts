export const contactEmail = "contact@robeson.org";
export function commentLink(title: string, path: string) {
  const subject = `Robeson comments: ${title}`;
  const body = `Document: https://robeson.org${path}\nSection or passage:\n\nComment or suggested wording:\n`;
  return contactEmail
    ? `mailto:${contactEmail}?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`
    : "/contact/";
}
