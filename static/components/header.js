var React = require('react');

var Header = React.createClass({
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

module.exports = Header;