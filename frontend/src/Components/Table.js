import * as React from 'react';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';

import './TraineesTable.css'

function createData(name, calories, fat, carbs, protein) {
  return { name, calories, fat, carbs, protein };
}


export default function BasicTable({heading,data}) {
    
  return (
    <TableContainer className='trainees-table' component={Paper}>
      <Table sx={{ minWidth: 650 }} aria-label="simple table">
        <TableHead>
          <TableRow>
            <TableCell>{heading[0]}</TableCell>
            <TableCell align="right">{heading[1]}</TableCell>
            <TableCell align="right">{heading[2]}</TableCell>
            <TableCell align="right">{heading[3]}</TableCell>
            <TableCell align="right">{heading[4]}</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {data.map((row) => (
            <TableRow
              key={row.name}
              sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
            >

              <TableCell component="th" scope="row">
                {row.name}
              </TableCell>
              <TableCell align="right">{row.progress}</TableCell>
              <TableCell align="right">{row.xp}</TableCell>
              <TableCell align="right">{row.grades}</TableCell>
              <TableCell align="right">{row.completed ? row.completed : '_'}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
}
