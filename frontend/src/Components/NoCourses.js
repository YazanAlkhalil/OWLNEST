import React from 'react'

function NoCourses() {
    return (
        <div className="flex w-full flex-col items-center ">
            <div className=" shadow-md rounded-lg p-8 max-w-md w-full">
                <div className="flex flex-col items-center">
                    <svg
                        className="h-16 w-16  mb-4"
                        fill="none"
                        viewBox="0 0 24 24"
                        stroke="currentColor"
                    >
                        <path
                            strokeLinecap="round"
                            strokeLinejoin="round"
                            strokeWidth={2}
                            d="M9 13h6m-3-3v6m-9 1V7a2 2 0 012-2h6l2 2h6a2 2 0 012 2v8a2 2 0 01-2 2H5a2 2 0 01-2-2z"
                        />
                    </svg>
                    <h2 className="text-2xl font-bold  mb-2">
                        No Courses Available
                    </h2>
                    <p className="mb-6">
                        It looks like there are no courses at the moment.
                    </p>
                </div>
            </div>
        </div>
    )
}

export default NoCourses
