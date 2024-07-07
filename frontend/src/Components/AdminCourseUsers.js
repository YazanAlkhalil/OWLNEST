import * as React from 'react';
import Box from '@mui/material/Box';
import Input from '@mui/material/Input';
import InputLabel from '@mui/material/InputLabel';
import InputAdornment from '@mui/material/InputAdornment';
import FormControl from '@mui/material/FormControl';
import TextField from '@mui/material/TextField';
import { BiSearch } from 'react-icons/bi';
import { FormControlLabel, Switch } from '@mui/material';
import UserInCourse from './UserInCourse';
function AdminCourseUsers() {
     const Data = [
        {
          name: 'John Doe',
          role: 'trainer',
          completionDate: null,
          isParticipant: true,
        },
        {
          name: 'Jane Smith',
          role: 'trainee',
          completionDate: '2023-05-15',
          isParticipant: true,
        },
        {
          name: 'Michael Johnson',
          role: 'trainee',
          completionDate: null,
          isParticipant: false,
        },
        {
          name: 'Emily Wilson',
          role: 'trainer',
          completionDate: '2023-03-20',
          isParticipant: true,
        },
        {
          name: 'David Thompson',
          role: 'trainee',
          completionDate: '2023-06-01',
          isParticipant: true,
        },
        {
          name: 'Sarah Anderson',
          role: 'trainer',
          completionDate: null,
          isParticipant: false,
        },
        {
          name: 'Robert Taylor',
          role: 'trainee',
          completionDate: '2023-04-10',
          isParticipant: true,
        },
      ];

const [data,setData] = React.useState(Data)
const [searchValue,setSearchValue] = React.useState('')
const [filteredData,setFilteredData] = React.useState([])
const [isParticipantOnly,setIsParticipantOnly] = React.useState(false)

const handleSearch = (e) => {
  setSearchValue(e.target.value.toLowerCase());
};
let tempData;
React.useEffect(()=>{
  if(searchValue !== ''){
    tempData = data.filter((user) =>
      user.name.toLowerCase().includes(searchValue))
  if(isParticipantOnly)
    tempData = tempData.filter((user) => user.isParticipant)
  setFilteredData(tempData)
  }
  else{
    if(isParticipantOnly){
      tempData = data.filter((user) => user.isParticipant)
      setFilteredData(tempData)
    }
    else{
      setFilteredData(data)
    }
  }
  
},[searchValue,isParticipantOnly])
    return (
        <div>
            <div className='my-10 flex justify-between'>

                <TextField
                    id="input-with-icon-textfield"
                    onChange={handleSearch}
                    value={searchValue}
                    InputProps={{
                        startAdornment: (
                            <InputAdornment position="start">
                                <BiSearch />
                            </InputAdornment>
                        ),
                    }}
                    variant="standard"
                />
                <FormControlLabel checked={isParticipantOnly} onChange={e=>setIsParticipantOnly(e.target.checked)} control={<Switch />} label="Participants only" />
            </div>
            <div className='grid grid-cols-4 py-2 rounded'>
                <div className='bg-secondary text-white p-4  rounded-l'>Name</div>
                <div className='bg-secondary text-white p-4 '>Role</div>
                <div className='bg-secondary text-white p-4 '>Completion date</div>
                <div className='bg-secondary text-white p-4  rounded-r'>Add/Remove</div>
            {filteredData.map((user,index) => (
                <UserInCourse key={JSON.stringify(user)} user={user} index={index}/>
            ))}
            </div>
        </div>
    )
}

export default AdminCourseUsers
