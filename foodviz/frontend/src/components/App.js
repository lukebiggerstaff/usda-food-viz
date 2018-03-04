import React, { Component  } from 'react';
import Nav from './Nav.js';
import SearchBar from './SearchBar.js';
import { Container } from 'reactstrap';

class App extends Component {
  render() {
    return (
      <div>
        <Nav />
        <Container>
          <SearchBar />
        </Container>
      </div>
    );
  }
}

export default App;
