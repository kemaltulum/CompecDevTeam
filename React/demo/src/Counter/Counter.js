import React, { Component } from 'react';
import './Counter.css';

class Counter extends Component {
  constructor(props) {
      super(props);
      this.state={numclick:0};
  }
  clicked() {
      this.setState({numclick:this.state.numclick+1});
  }
  render() {
    return (
      <div className="Counter">
        <button onClick={this.clicked.bind(this)}>
        {this.state.numclick}
        </button>
      </div>
    );
  }
}

export default Counter;
