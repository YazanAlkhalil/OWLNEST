import React from 'react';

const Notification = ({ notification }) => (
    <div className={`flex items-center p-4 rounded-lg mb-4 ${notification.is_read
        ? 'bg-white'
        : 'bg-blue-50 border-l-4 border-blue-500'
        }`}>
        <div className="flex-shrink-0 mr-4">
            {notification.image ? (
                <img
                    src={notification.image}
                    alt={`${notification.username}'s avatar`}
                    className="w-12 h-12 rounded-full object-cover"
                />
            ) : (
                <div className="w-12 h-12 bg-gray-300 rounded-full flex items-center justify-center">
                    <span className="text-xl text-gray-600">{notification.username[0].toUpperCase()}</span>
                </div>
            )}
        </div>
        <div className="flex-grow">
            <p className={`text-sm ${notification.is_read ? 'text-gray-600' : 'text-gray-900 font-medium'
                }`}>
                {notification.message}
            </p>
            <p className="text-xs text-gray-500">
                {notification.username} • {notification.time_since_sent}
            </p>
        </div>
        {!notification.is_read && (
            <div className="flex-shrink-0 ml-4">
                <span className="inline-block w-2 h-2 bg-blue-600 rounded-full"></span>
            </div>
        )}
    </div>
);

const NotificationList = ({ notifications }) => {
    return (
        <div className="bg-gray-300 px-4 py-2 rounded absolute right-10 max-h-[50vh] overflow-auto w-96 mx-auto mt-4">
            {notifications.map((notification) => (
                <Notification key={notification.id} notification={notification} />
            ))}
        </div>
    );
};

export default NotificationList;