import Reflux from 'reflux';
import authActions from '../actions/auth';

let authStore = Reflux.createStore({
  init: function () {
    this.listenTo(authActions.signup, this.signup);
    this.listenTo(authActions.login, this.login);
    this.listenTo(authActions.logout, this.logout);
  },
  getInitialState: function () {
    return {};
  }
});

export default authStore;