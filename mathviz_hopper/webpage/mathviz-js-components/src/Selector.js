import React, { Component } from 'react';
import 'react-select/dist/react-select.css'
import Select from 'react-select';
import {formatMath} from './helpers'
// import {get_katex} from '../actions/action_helpers'


class Selector extends React.Component {
  
  constructor(props) {
    super(props)
    this.state = {
                  value: {
                    value: null,
                    label: null
                  }
                }
    this.onChange = this.onChange.bind(this)
    this.handleQueryChange=this.handleQueryChange.bind(this)
  }


  onChange(value) {

    if(!value) {
      this.setState({ value: {value: null, label: null} } );
      return
    }

    this.setState({ value: {value: value, label: formatMath(value)}});
    this.props.query(value)

  } 

  handleQueryChange(input) {
    this.props.getSuggestions(input)
  }

  render () {
    console.log("rendered selector")
    console.log(this.props)
    return (
      <Select
          style = {{height:60} }
          onChange={this.onChange}
          options={this.props.options}
          simpleValue
          value={this.state.value}
          onInputChange={this.handleQueryChange}

      />
      
    );
  }
}




export default Selector;