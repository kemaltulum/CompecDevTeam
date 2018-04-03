import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import LoginPage from './LoginPage/LoginPage.js'
import ClockBox from './ClockBox/ClockBox.js'
import Counter from './Counter/Counter.js'

class App extends Component {
  handleMessage(data) {
      this.setState({price:data.price});
  }
  handleError() {
      this.setState({price:"ERROR"});      
  }
  handleOpen() {
      this.wsocket.send("{\"product_ids\":[\"btc-usd\"],\"type\":\"subscribe\"}");
  }
  constructor(props) {
      super(props);
      this.wsocket = new WebSocket("wss://ws-feed.gdax.com/");
      this.wsocket.onopen = this.handleOpen.bind(this);
      this.wsocket.onmessage = function(event) {
          this.handleMessage(JSON.parse(event.data));
      }.bind(this);
      this.wsocket.onerror = this.handleError.bind(this);
      this.state={price:"UNK"};
  }
  render() {
    return (
      <div className="App">
	   <ClockBox clock="18:15" message="Merhaba!"/>
	   <Counter/>
         <div className="PriceClass">
             {this.state.price}
         </div>
      </div>
    );
  }
}

export default App;
