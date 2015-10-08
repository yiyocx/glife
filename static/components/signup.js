import React from 'react';

export default React.createClass({
  render: function () {
    return (
      <div className="row">
        <form className="col s6">
          <div className="row">
            <div className="input-field col s6">
              <input id="first_name" type="text" className="validate"/>
              <label htmlFor="first_name">Nombre</label>
            </div>
            <div className="input-field col s6">
              <input id="last_name" type="text" className="validate"/>
              <label htmlFor="last_name">Apellidos</label>
            </div>
          </div>
          <div className="row">
            <div className="input-field col s12">
              <input id="email" type="email" className="validate" required="" aria-required="true"/>
              <label htmlFor="email">Correo Electrónico</label>
            </div>
          </div>
          <div className="row">
            <div className="input-field col s6">
              <input id="phone_number" type="text" className="validate"/>
              <label htmlFor="phone_number">Número Telefónico</label>
            </div>
            <div className="input-field col s6">
              <input id="birthday" type="date" className="datepicker"/>
              <label htmlFor="birthday" className="active">Fecha de Nacimiento</label>
            </div>
          </div>
          <div className="row">
            <div className="input-field col s6">
              <input id="password" type="password" className="validate"/>
              <label htmlFor="password">Contraseña</label>
            </div>
            <div className="input-field col s6">
              <input id="re_password" type="password" className="validate"/>
              <label htmlFor="re_password">Repita la Contraseña</label>
            </div>
          </div>
          <div className="input-field col s12">
            <button className="btn waves-effect waves-light" type="submit" name="action">Register</button>
          </div>
        </form>
      </div>
    );
  }
});