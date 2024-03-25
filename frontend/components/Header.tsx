import Link from "next/link";


const Header = () => {
    return (
        <header>
            <nav>
                <ul>
                    <li>
                        <Link href={ '/' }>
                            WikiNetes
                        </Link>
                    </li>
                    <li></li>
                    <li></li>
                    <li></li>
                    <li></li>
                </ul>
            </nav>
        </header>
    )
}

export default Header