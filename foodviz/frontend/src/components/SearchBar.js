import React, { Component } from 'react';
import SearchInput from './SearchInput';
import SearchButton from './SearchButton';

class SearchBar extends Component {
  render() {
    return (
      <div>
        <form className="form-group" action="">
          <div className="input-group ">
            <SearchInput />
            <SearchButton />
          </div>
        </form>
      </div>
    );
  }
}

export default SearchBar;
