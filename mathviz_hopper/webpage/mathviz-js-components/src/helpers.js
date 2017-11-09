import React, { Component } from 'react';
// import katex from './katex'
const katex = require(`katex.js`)
export const formatMath = (text) => {
  try {
  	  // console.log(katex)
      const obj = katex.renderToString(text, { throwOnError: false, falsetrackLocation: true})
      return <span dangerouslySetInnerHTML={{__html: obj}} />
  }
  catch(err) {
  	console.log("error")
    return text
  }
}

export const get_path = (asset) => {
	/*
	gets the proper load path for assets
	*/
	const parent_path = window.location.href.replace(/\/[^\/]{0,}$/, "")
    return `${parent_path+process.env.PUBLIC_URL.substr(1)+"/"+asset}`
}