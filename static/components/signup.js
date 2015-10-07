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
              <input id="last_name" type="text" className="validate"/>
              <label htmlFor="last_name">Fecha de Nacimiento</label>
            </div>
            <div className="input-field col s6">
              <input id="last_name" type="text" className="validate"/>
              <label htmlFor="last_name">Número Telefónico</label>
            </div>
          </div>
          <div className="row">
            <div className="input-field col s6">
              <input id="password" type="password" className="validate"/>
              <label htmlFor="password">Contraseña</label>
            </div>
            <div className="input-field col s6">
              <input id="last_name" type="password" className="validate"/>
              <label htmlFor="re_password">Repita la Contraseña</label>
            </div>
          </div>
          <div className="input-field col s12">
            <button className="btn waves-effect waves-light" type="submit" name="action">Submit</button>
          </div>
        </form>
      </div>
    );
  }
});