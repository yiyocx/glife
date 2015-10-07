import React from 'react'

// Routing
import {Router, Route, Link, IndexRoute} from 'react-router'

// View Components
import Template from './components/template'
import HelloWorld from './components/HelloWorld'

let routes = (
  <Router>
    <Route path="/" component={Template}>
      <IndexRoute component={HelloWorld} />
    </Route>
  </Router>
);

export default routes;