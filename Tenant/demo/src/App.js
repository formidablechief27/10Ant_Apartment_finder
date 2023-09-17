import './App.css';
import React from 'react';
import axios from 'axios';

class App extends React.Component {
  state = {details: [],}

  componentDidMount() {
    let data;
    axios.get('http://127.0.0.1:8000/apartment/')
    .then(res => {
      console.log(res);
      data = res.data;
      this.setState({details: data});
    })
    .catch(err => {
      console.log(err);
    });
  }
  
  render() {
    return (
      <div className="App">
        <header>My React App</header>
        
        <div>
          <h2>My Django API</h2>
          {this.state.details.map(item => (
            <div key={item.id}>
              <p>{item.title}</p>
              <p>{item.address}</p>
              <p>{item.price}</p>
            </div>
          ))}
        </div>
      </div>
    );
  }
}

export default App;
