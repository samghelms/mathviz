import React, { Component } from 'react';
import ReactTable from 'react-table'
import 'react-table/react-table.css'

const cell_style={
        fontSize: '0.7em',
      }

const TableWrap = ({data, columns}) => {
	console.log("rendered table")
	return (
		<div>
			<ReactTable
			    data={data}
		        columns = {columns}
			  />
		</div>
	)
}

export default TableWrap;