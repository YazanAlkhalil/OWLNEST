import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import Comment from '../Comment';
import AddComment from '../AddComment';
import useFetch from '../AuthComponents/UseFetch';

export default function TraineeDiscussion() {
  const { fetchData } = useFetch();
  const { id } = useParams();
  const [comments, setComments] = useState([]);

  useEffect(() => {
    console.log(id);
    const getComments = async () => {
      const res = await fetchData({ url: 'http://127.0.0.1:8000/api/course/' + id + '/comments', method: 'get' });
      setComments(res);
    };
    getComments();
  }, [fetchData, id]);

  const addNewComment = (newComment) => {
    setComments((prevComments) => [...prevComments,newComment]);
  };

  return (
    <>
      <div className='flex justify-end py-5'>
        <AddComment addNewComment={addNewComment} />
      </div>
      <div>
        {comments.map((com) => {
          return <Comment key={com.id} data={com} />;
        })}
      </div>
    </>
  );
}
