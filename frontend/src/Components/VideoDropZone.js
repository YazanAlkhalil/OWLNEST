import React, { useCallback, useState } from 'react';
import { useDropzone } from 'react-dropzone';
import ProgressBar from './ProgressBar';

const VideoDropzone = ({ type }) => {
    const [uploadedFile, setUploadedFile] = useState(null);
    const [uploadSuccess, setUploadSuccess] = useState(false);
    const [fileRejectionMessage, setFileRejectionMessage] = useState('');
    const [uploadProgress, setUploadProgress] = useState(0);
    const types = Object.keys(type)

    const onDrop = useCallback((acceptedFiles, rejectedFiles) => {

        if (acceptedFiles.length === 1 && rejectedFiles.length === 0) {
            const file = acceptedFiles[0];
            setUploadedFile(file);
            setFileRejectionMessage('');
            setUploadProgress(0);
            setUploadSuccess(false);
            const reader = new FileReader();

            reader.onabort = () => console.log('file reading was aborted');
            reader.onerror = () => console.log('file reading has failed');
            reader.onprogress = (event) => {
                if (event.lengthComputable) {
                    const progress = Math.round((event.loaded * 100) / event.total);
                    setUploadProgress(progress);
                }
            };
            reader.onload = () => {
                    setUploadProgress(100);
                    setUploadSuccess(true);
            };
            reader.readAsDataURL(file);
        } else if (rejectedFiles.length > 0) {
            setUploadedFile(null);
            setFileRejectionMessage(`Please upload a valid video file ${type[types[0]]}`);
            setUploadProgress(0);
            setUploadSuccess(false);

        }
    }, []);

    const {
        getRootProps,
        getInputProps,
        isDragActive,
        isDragReject,
    } = useDropzone({
        onDrop,
        accept: type,
        maxFiles: 1,
    });

    return (
        <div className="flex flex-col items-center justify-center">
            <div
                {...getRootProps()}
                className={`dropzone mx-auto mt-8 w-full max-w-lg rounded-md border-2 border-dashed py-12 px-6 text-center transition-colors ${isDragActive
                    ? 'border-green-500 bg-green-100'
                    : isDragReject
                        ? 'border-red-500 bg-red-100'
                        : 'border-gray-300 bg-gray-100'
                    }`}
            >
                <input {...getInputProps()} />
                {isDragActive ? (
                    <p className="text-green-700">Drop the video file here...</p>
                ) : isDragReject ? (
                    <p className="text-red-700">Invalid file type. Please drop a video file only.</p>
                ) : uploadedFile ? (
                    <div>
                        {uploadSuccess ? (
                            <div>
                                <p className="text-green-700">File uploaded successfully!</p>
                                <p className="text-gray-700">{uploadedFile.name}</p>
                            </div>
                        ) : (
                            <div>
                                <p className="text-gray-600">Uploading...</p>
                                <p className="text-gray-700">{uploadedFile.name}</p>
                                <ProgressBar progress={uploadProgress} />
                            </div>
                        )}
                    </div>
                ) : (
                    <div>
                        <p className="mb-2 text-gray-600">
                            Drag and drop a video file here, or click to select a file
                        </p>
                        <p className="text-gray-400">(Supported formats: {type[types[0]].map(item => item + " ")})</p>
                    </div>
                )}
            </div>
            {fileRejectionMessage && (
                <div className="mt-4 w-full max-w-md">
                    <p className="text-red-500">{fileRejectionMessage}</p>
                </div>
            )}
        </div>
    );
};

export default VideoDropzone;