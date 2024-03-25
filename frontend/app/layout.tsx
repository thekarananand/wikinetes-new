import type { Metadata } from "next";
import { inter } from '@/font/inter.js';
import "@/styles/core-styles.css";


export  const metadata: Metadata = {
    title: "WikiNetes",
    description: "WikiNetes is a free online article sharing platform service.",
};

export default function RootLayout({ children,}: Readonly < { children: React.ReactNode; } > ) {
    return (
        <html lang="en">
            <body className={inter.className}>{children}</body>
        </html>
    );
}