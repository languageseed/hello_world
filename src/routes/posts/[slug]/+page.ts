// Prerender during build only
export const prerender = process.env.NODE_ENV === 'production' ? true : 'auto';

