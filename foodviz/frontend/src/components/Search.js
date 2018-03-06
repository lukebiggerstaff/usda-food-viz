import React, { Component } from 'react';
import SearchInput from './SearchInput';
import SearchResultList from './SearchResultList';

class Search extends Component {
  constructor(props){
    super(props);
    this.state = {
      searchTerm: '',
      searchData: null,
    }
    this.handleChange = this.handleChange.bind(this);
  }

  handleChange(event){
    const term = event.target.value;
    this.updateSearchTerm(term);
    this.updateSearchData(term);
  }

  updateSearchTerm(term){
    this.setState({
      searchTerm: term,
    });
  }

  updateSearchData(term){
    if (term.length < 4){
      this.setState({
        searchData: null,
      });
      return;
    }
    if (this.timeout) clearTimeout(this.timeout);
    this.timeout = setTimeout(() => {
      fetch(`/api/search/?query=${term}`).then(
        res => res.json()
      ).then(
        data => this.setState({
          searchData: data.slice(0, 20),
        })
      );
    }, 400);
  }

  render() {
    return (
      <div>
        <form className="form-group" action="">
          <SearchInput value={this.state.searchTerm} onChange={this.handleChange} />
          <SearchResultList data={this.state.searchData} />
        </form>
      </div>
    );
  }
}

export default Search;
