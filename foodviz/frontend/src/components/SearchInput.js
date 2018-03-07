import React, { Component } from 'react';
import '../styles/SearchInput.css';

class SearchInput extends Component {
  render() {
    return (
      <input value={this.props.value} onChange={this.props.onChange} 
      placeholder="Type to begin searching... and click the chart for more info" className="form-control form-control-lg" />
    );
  }
}

export default SearchInput;
