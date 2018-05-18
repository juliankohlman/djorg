import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import axios from 'axios';

class App extends Component {
  state = {
    notes: []
  };

  // async componentDidMount() {
  //   try {
  //     const res = await fetch('http://127.0.0.1:8000/api/');
  //     const notes = await res.json();
  //     this.setState({notes})
  //   } catch (e) {
  //     console.log(e);
  //   }
  // }
  componentDidMount() {
    axios.get('http://127.0.0.1:8000/api/')
      .then(res => {
        const notes = res.data;
        this.setState({ notes });
      })
  }
  

  render() {
    return (
      <ol>
        { this.state.notes.map(note => 
          <li>
            <h2>{note.title}</h2>
              <p>{note.content}</p>
          </li>)}
      </ol>
    );
  }
}

export default App;
