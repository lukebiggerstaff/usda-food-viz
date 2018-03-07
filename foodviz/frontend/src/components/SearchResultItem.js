import React, { Component } from 'react';
import '../styles/SearchResultItem.css';

class SearchResultListItem extends Component {
  render () {
    return (
      <li 
        className="search-result-name"
        key={this.props.key}>
        {this.props.name}
      </li>
    );
  }
}
