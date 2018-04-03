import React, { Component } from 'react';
import './ClockBox.css';

class ClockBox extends Component {
  render() {
    return (
      <div className="ClockBox">
	   <div class="clock">
            {this.props.clock}
        </div>
        {this.props.message}
      </div>
    );
  }
}

export default ClockBox;
