import React, { Component } from 'react';

class SearchResultListItem extends Component {
  render () {
    return (
      <li key={this.props.key}>
        {this.props.name}
      </li>
    );
  }
}
