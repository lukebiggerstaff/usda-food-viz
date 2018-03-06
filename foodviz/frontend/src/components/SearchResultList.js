import React, { Component } from 'react';
import SearchResultListItem from './SearchResultListItem';


class SearchResultList extends Component {
  render() {
    if (this.props.data){ 
      this.searchResultListItems = this.props.data.map((item) => {
        return (
          <SearchResultListItem 
            key={item["ndb_no"]}
            name={item["description"]}
            data={item}
          />
        );
      }); 
      return (
        <div>
          {this.searchResultListItems}
        </div>
      );
    } else {
      return null;
    }
  }
}

export default SearchResultList;
