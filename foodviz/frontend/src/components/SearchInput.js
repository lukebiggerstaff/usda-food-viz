import React, { Component } from 'react';

class SearchInput extends Component {
  render() {
    return (
      <input value={this.props.value} onChange={this.props.onChange} 
      placeholder="Type to begin searching..." className="form-control form-control-lg" />
    );
  }
}

export default SearchInput;
