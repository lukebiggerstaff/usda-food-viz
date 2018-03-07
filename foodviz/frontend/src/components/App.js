import React, { Component  } from 'react';
import Nav from './Nav.js';
import Search from './Search.js';
import { Container } from 'reactstrap';

class App extends Component {
  render() {
    return (
      <div>
        <Nav />
        <Container>
          <Search />
        </Container>
      </div>
    );
  }
}

export default App;
