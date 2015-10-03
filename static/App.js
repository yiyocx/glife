var React = require('react');
// Routing
var Router = require('react-router');
var Route = Router.Route;
var RouteHandler = Router.RouteHandler;
var DefaultRoute = Router.DefaultRoute;
// View Components
var HelloWorld = require('./components/HelloWorld');

var AppManager = React.createClass({
  render: function() {
    return (
      <RouteHandler/>
    );
  }
});

var routes = (
  <Route handler={ AppManager } >
    <DefaultRoute name="home" handler={ HelloWorld } />
  </Route>
);

Router.run(routes, function(Handler) {
  React.render(<Handler/>, document.body);
});