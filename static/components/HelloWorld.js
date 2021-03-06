var React = require('react');

var HelloWorld = React.createClass({
  render: function() {
    return(
      <div>
        <div className="row">
          <div className="col s12 m6">
            <div className="card blue-grey darken-1">
              <div className="card-content white-text">
                <span className="card-title">Hello, React World!</span>
                <p>I am a very simple card. I am very good at containing small bits of information.
                I am convenient because I require little markup to use effectively.</p>
              </div>
              <div className="card-action">
                <a href="#">This is a link</a>
                <a href="#">This is a link</a>
              </div>
            </div>
          </div>
        </div>
      </div>
    );
  }
});

module.exports = HelloWorld;