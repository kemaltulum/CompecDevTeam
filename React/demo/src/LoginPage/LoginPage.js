import React, { Component } from 'react';
import './LoginPage.css';

class LoginPage extends Component {
  login() {
    var msg = {}
    msg["subject"] = "LoginPasswordEntered";
    msg["password"] = this.passwordInput.value;
    this.props.wsocket.send(JSON.stringify(msg));
    this.passwordInput.value="";
    this.passwordInput.select();
  }
  onSubmit(e) {
    e.preventDefault();
    this.login();
    return false;
  }
  onKeyPress(e) {
    if (e.key === "Enter") {
      e.preventDefault();
      this.login();
      return false;
    }
  }
  onPasswordInputMounted(passwordInput) {
    this.passwordInput = passwordInput;
    if (passwordInput !== null)
      passwordInput.select();
  }
  render() {
    return (
      <div className="LoginPage">
        <span>{this.props.message}</span>
        <br/>
        <span>Password:</span>
        <input type="password" onKeyPress={this.onKeyPress.bind(this)} ref={this.onPasswordInputMounted.bind(this)}/>
        <button onClick={this.onSubmit.bind(this)}>Submit</button>
      </div>
    );
  }
}

export default LoginPage;
