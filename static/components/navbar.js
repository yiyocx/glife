import React from 'react';
import Reflux from 'reflux';
import Link from 'react-router';
import authStore from '../stores/auth';

let NavBar = React.createClass({
  mixins: [Reflux.connect( authStore, 'user' )],

  render: function () {
    return (
      <nav>
        <div className="nav-wrapper cyan z-depth-1">
          <a href="/" className="brand-logo">Glife</a>
          <ul id="nav-mobile" className="right hide-on-med-and-down">
            <li className="active"><a href="#">Inicio</a></li>
            <li><a href="#">Registrarse</a></li>
            <li><a href="#">Iniciar Sesión</a></li>
          </ul>
        </div>
      </nav>
    );
  }
});

export default NavBar;