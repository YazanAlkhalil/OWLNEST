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
import useFetch from '../Components/AuthComponents/UseFetch'
import { useParams } from 'react-router-dom';


function AdminCourseUsers() {
  const { fetchData } = useFetch()
  const { id } = useParams()
  const getUsers = async () => {
    const res = await fetchData({ url: 'http://127.0.0.1:8000/api/course/' + id + '/all-users' })
    setFilteredData(res)
    setData(res)
  }
  React.useEffect(() => {
    getUsers()
  }, [])

  const [data, setData] = React.useState([])
  const [searchValue, setSearchValue] = React.useState('')
  const [filteredData, setFilteredData] = React.useState([])
  const [isParticipantOnly, setIsParticipantOnly] = React.useState(false)

  const handleSearch = (e) => {
    setSearchValue(e.target.value.toLowerCase());
  };
  let tempData;
  React.useEffect(() => {
    if (searchValue !== '') {
      tempData = data.filter((user) =>
        user.username.toLowerCase().includes(searchValue))
      if (isParticipantOnly)
        tempData = tempData.filter((user) => user.is_participant)
      setFilteredData(tempData)
    }
    else {
      if (isParticipantOnly) {
        tempData = data.filter((user) => user.is_participant)
        setFilteredData(tempData)
      }
      else {
        setFilteredData(data)
      }
    }

  }, [searchValue, isParticipantOnly])
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
        <FormControlLabel checked={isParticipantOnly} onChange={e => setIsParticipantOnly(e.target.checked)} control={<Switch />} label="Participants only" />
      </div>
      <div className='grid grid-cols-4 py-2 rounded'>
        <div className='bg-secondary text-white p-4  rounded-l'>Name</div>
        <div className='bg-secondary text-white p-4 '>Role</div>
        <div className='bg-secondary text-white p-4 '>Completion date</div>
        <div className='bg-secondary text-white p-4  rounded-r'>Add/Remove</div>
        {filteredData.map((user, index) => (
          <UserInCourse getUsers={getUsers} key={user.id} user={user} index={index} />
        ))}
      </div>
    </div>
  )
}

export default AdminCourseUsers
