import { useEffect, useState } from 'react'
import FormDialog from '../../Components/admin/AddUserDialog'
import { InputAdornment, TextField } from '@mui/material'
import { BiSearch } from 'react-icons/bi'
import UserInCourseAdmin from '../../Components/UserInCourseAdmin';
import useFetch from '../../Components/AuthComponents/UseFetch';

function AdminUsers() {
  const [searchValue, setSearchValue] = useState('');
  const [filteredData, setFilteredData] = useState([]);
  const isOwner = localStorage.getItem('isOwner');
  const { fetchData } = useFetch();
  const companyId = localStorage.getItem('companyId');

  const fetchUsers = async () => {
    const data = await fetchData({ url: "http://127.0.0.1:8000/api/company_users/"+companyId });
    console.log(data);
    setFilteredData(data);
  };
  useEffect(() => {
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
      fetchData({ url: "http://127.0.0.1:8000/api/company_users/"+companyId }).then(setFilteredData);
    }
  }, [searchValue]);

  return (
    <div>
      <div className='flex justify-between items-center'>
        <FormDialog fetchUsers={fetchUsers} className='self-start' />
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
        <div className='bg-secondary dark:bg-DarkSecondary text-white p-4 rounded-l'>Name</div>
        <div className='bg-secondary dark:bg-DarkSecondary text-white p-4'>Roles</div>
        <div className='bg-secondary dark:bg-DarkSecondary text-white p-4'>Last login</div>
        <div className='bg-secondary dark:bg-DarkSecondary text-white p-4 rounded-r'>Actions</div>
        {filteredData.map((user, index) => (
          <UserInCourseAdmin isOwner={isOwner} key={user.id} fetchUsers={fetchUsers} index={index} user={user} />
        ))}
      </div>
    </div>
  );
}

export default AdminUsers
