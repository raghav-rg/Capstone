import React from 'react'
import NavbarLink from './NavbarLink'

function NavigationBar() {
  return (
    <div id="navbar">
        <div className="navtitle">ForTrade</div>
        <div id="navlinks">
            <NavbarLink path="/" text="Home"/>
            <NavbarLink path="/dashboard" text="Dashboard"/>
        </div>
    </div>
  )
}

export default NavigationBar