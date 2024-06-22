import {useEffect, useState} from 'react'
import FormDialog from '../../Components/admin/AddUserDialog'
import { InputAdornment, TextField } from '@mui/material'
import { BiSearch } from 'react-icons/bi'
import UserInCourseAdmin from '../../Components/UserInCourseAdmin';

function AdminUsers() {
  const Data = [
    {
      name: 'John Doe',
      role: 'trainer',
      completionDate: "2033-2-3",
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
      completionDate: "2033-2-3",
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
      completionDate: "2033-2-3",
      isParticipant: false,
    },
    {
      name: 'Robert Taylor',
      role: 'trainee',
      completionDate: '2023-04-10',
      isParticipant: true,
    },
  ];
  const [searchValue,setSearchValue] = useState('')
  const [filteredData,setFilteredData] = useState([])
  let tempData;
  useEffect(()=>{
    if(searchValue !== ''){
      let search = searchValue.toLowerCase()
      tempData = Data.filter((user) =>
        user.name.toLowerCase().includes(search))
      console.log(tempData);
    setFilteredData(tempData)
    }
    else{
        setFilteredData(Data)
    }
  },[searchValue])

  return (
    <div >
      <div className='flex justify-between items-center'>

        <FormDialog className='self-start' />
        <TextField
          id="input-with-icon-textfield"
          onChange={e=>setSearchValue(e.target.value)}
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
      </div>
      <div className='grid grid-cols-4'>
        <div className='bg-secondary text-white p-4  rounded-l'>Name</div>
        <div className='bg-secondary text-white p-4 '>Role</div>
        <div className='bg-secondary text-white p-4 '>Last login</div>
        <div className='bg-secondary text-white p-4  rounded-r'>Actions</div>
        {filteredData.map((user, index) => <UserInCourseAdmin key={JSON.stringify(user)} index={index} user={user} />)}
      </div>
    </div>
  )
}

export default AdminUsers
