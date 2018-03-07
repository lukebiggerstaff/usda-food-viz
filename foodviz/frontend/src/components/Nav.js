import React from 'react';
import {Navbar, NavbarBrand} from 'reactstrap';
import '../styles/Nav.css';

const Nav = () => {
  return (
    <div>
      <Navbar className="navbar">
        <NavbarBrand className="navbar-brand">FoodViz</NavbarBrand>
      </Navbar>
    </div>
  );
}
export default Nav;
