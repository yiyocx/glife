import React from 'react';
import NavBar from './navbar'
import Signup from './signup'

let Template = React.createClass({
  render: function () {
    return (
      <div>
        <NavBar/>
        <Signup/>
      </div>
    );
  }
});

export default Template;