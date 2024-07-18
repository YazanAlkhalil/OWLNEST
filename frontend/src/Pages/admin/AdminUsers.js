import { useEffect, useState } from 'react'
import FormDialog from '../../Components/admin/AddUserDialog'
import { InputAdornment, TextField } from '@mui/material'
import { BiSearch } from 'react-icons/bi'
import UserInCourseAdmin from '../../Components/UserInCourseAdmin';
import useFetch from '../../Components/AuthComponents/UseFetch';

function AdminUsers() {
  const [searchValue, setSearchValue] = useState('');
  const [filteredData, setFilteredData] = useState([]);
  const { fetchData } = useFetch();

  useEffect(() => {
    const fetchUsers = async () => {
      const data = await fetchData({ url: "http://127.0.0.1:8000/api/company_users/2" });
      setFilteredData(data);
    };
    fetchUsers();
  }, []);

  useEffect(() => {
    if (searchValue !== '') {
      const search = searchValue.toLowerCase();
      const tempData = filteredData.filter((user) =>
        user.username.toLowerCase().includes(search)
      );
      setFilteredData(tempData);
    } else {
      // Reset to original data
      fetchData({ url: "http://127.0.0.1:8000/api/company_users/2" }).then(setFilteredData);
    }
  }, [searchValue]);

  return (
    <div>
      <div className='flex justify-between items-center'>
        <FormDialog className='self-start' />
        <TextField
          id="input-with-icon-textfield"
          onChange={e => setSearchValue(e.target.value)}
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
        <div className='bg-secondary text-white p-4 rounded-l'>Name</div>
        <div className='bg-secondary text-white p-4'>Roles</div>
        <div className='bg-secondary text-white p-4'>Last login</div>
        <div className='bg-secondary text-white p-4 rounded-r'>Actions</div>
        {filteredData.map((user, index) => (
          <UserInCourseAdmin key={user.id} index={index} user={user} />
        ))}
      </div>
    </div>
  );
}

export default AdminUsers
