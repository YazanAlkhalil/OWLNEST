import React, { useEffect, useRef, useState } from 'react'
import { IoMdClose } from "react-icons/io";
import CustomizedSlider from './CustomizedSlider';
import { Button, Dialog, DialogActions, DialogContent, DialogTitle } from '@mui/material';
import Skill from './Skill';
import useFetch from './AuthComponents/UseFetch';
import { useParams } from 'react-router-dom';
function AdditionalInfo({ close }) {
  const [name,setName]=useState("")
  const [value,setValue]=useState(20)
  const [resources,setResources] = useState("")
  const [description,setDescription] = useState("")
  const [skills,setSkills] = useState([])
  const {fetchData} = useFetch()
  const {id} = useParams()

  const textareaRef = useRef(null);


  const [open, setOpen] = useState(false)
  const handleClickOpen = () => {
    setOpen(true);
  };

  const handleClose = () => {
    setOpen(false);
  };

  async function getData(){
    const res = await fetchData({url:"/course/"+id+"/skills"})
    setSkills(res)
    const rse = await fetchData({url:"/course/"+id+"/additional-resources"})
    setResources(rse.text)
    const desc = await fetchData({url:"/course/"+id})
    setDescription(desc.description)
  }
  useEffect(() => {
    getData()
    const adjustHeight = () => {
      textareaRef.current.style.height = 'auto';
      textareaRef.current.style.height = `${textareaRef.current.scrollHeight + 2}px`;
    };

    adjustHeight();

    const textarea = textareaRef.current;
    textarea.addEventListener('input', adjustHeight);

    return () => {
      textarea.removeEventListener('input', adjustHeight);
    };
  }, []);

  async function addSkill(){
    await fetchData({url:"/course/"+id+"/skills",method:"POST",data:{skill:name,rate:value}})
    reset()
  } 
  function reset(){
    setOpen(false)
    setName("")
    setValue(0)
  } 
  async function handleSubmit(){
    fetchData({url:"/course/"+id,method:"PATCH",data:{description}})
    fetchData({url:"/course/"+id+"/additional-resources",method:"POST",data:{text:resources}})
    close()
  }

  return (

    <div className='flex flex-col'>

      <IoMdClose className='self-end hover:cursor-pointer size-7' onClick={close} />
      <React.Fragment>
        <button className='self-start mb-6 h-auto text-xl border border-solid border-secondary p-3 hover:bg-secondary hover:text-white rounded  text-secondary sticky top-1' onClick={handleClickOpen}>
          Add Skill
        </button>
        <Dialog
          open={open}
          onClose={handleClose}
          PaperProps={{
            component: 'form',
            onSubmit: (event) => {
              event.preventDefault();
            },
          }}
        >
          <DialogTitle>Add Skill Info</DialogTitle>
          <DialogContent >
            <div className='flex flex-col'>
              <CustomizedSlider name={name} setName={setName} value={value} setValue={setValue}/>
            </div>
          </DialogContent>
          <DialogActions>
            <Button onClick={reset} >Cancel</Button>
            <Button onClick={addSkill} type="submit">Add</Button>
          </DialogActions>
        </Dialog>
      </React.Fragment>
      {skills.map(skill => (
        <Skill name={skill.skill} value={skill.rate}/>
      ))}
      <textarea
        className='p-2 border-solid mb-6 mt-10 border dark:bg-Gray  border-gray-400'
        ref={textareaRef}
        rows="4"
        placeholder="Add Additional Resources"
        style={{ resize: 'none' }}
        value={resources}
        onChange={e=>setResources(e.target.value)}
      />
      <textarea
        className='p-2 border-solid border dark:bg-Gray  border-gray-400'
        ref={textareaRef}
        rows="4"
        placeholder="Add Description"
        style={{ resize: 'none' }}
        value={description}
        onChange={e=>setDescription(e.target.value)}
      />
      <button onClick={handleSubmit} className='self-end border rounded p-2 mt-6 text-xl  hover:bg-white hover:text-black inner-btn'>Save</button>
    </div>
  )
}

export default AdditionalInfo
