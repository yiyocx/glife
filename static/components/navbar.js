import React from 'react';
import Reflux from 'reflux';
import Link from 'react-router';
import authStore from 'stores/auth';

let NavBar = React.createClass({
  mixins: [
    State,
    Reflux.connect( authStore, 'user' )
  ],

  render: function () {
    return (
      <nav>
        <div className="nav-wrapper cyan z-depth-1">
          <a href="/" className="brand-logo">Glife</a>
          <ul id="nav-mobile" className="right hide-on-med-and-down">
            <li className="active"><a href="#">Menu 1</a></li>
            <li><a href="#">Menu 2</a></li>
            <li><a href="#">Menu 3</a></li>
          </ul>
        </div>
      </nav>
    );
  }
});

export default NavBar;