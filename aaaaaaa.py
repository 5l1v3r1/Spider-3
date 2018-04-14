clear; % % % % % 这个程序是用来调取这三个指数的数据，以此来计算当日基差

StartDate = '2016-02-19';
EndDate = '2018-01-18';
% 这里是调取基差数据

% Index = '000300.SH'; % % % % '000300.SH', '000016.SH', '000905.SH'
w = windmatlab;
label = '.CFE';
IndexLabel = 'IC';
Future_K1 = '00';
Future_K2 = '01';
Future_K3 = '02';
Future_K4 = '03';

Future0 = strcat(IndexLabel, label); % 这五个分别是对应指数的指数值，本月连续值，下月连续值，本季连续值，下季连续值
Future1 = strcat(IndexLabel, Future_K1, label);
Future2 = strcat(IndexLabel, Future_K2, label);
Future3 = strcat(IndexLabel, Future_K3, label);
Future4 = strcat(IndexLabel, Future_K4, label);

Name = strcat(IndexLabel, label);
if strcmp(IndexLabel, 'IC')
    Index = '000905.SH';
    SheetName = '中证500';
    % StartDate = '2015-04-16';
    time_p = [{'2015-07-08'}, {'2015-08-03'}, {'2015-08-26'}, {'2015-08-27'}, {'2015-08-28'}, {'2015-08-31'},
              {'2015-09-07'}, {'2016-01-08'}, {'2017-02-17'}]
    ';

elseif
strcmp(IndexLabel, 'IF')
Index = '000300.SH';
SheetName = '沪深300';
% StartDate = '2010-04-16';
time_p = [{'2010-07-16'}, {'2011-01-21'}, {'2011-04-15'}, {'2011-07-15'}, {'2011-08-08'}, {'2011-10-21'},
          {'2012-01-20'}, {'2012-04-20'}, ...
          {'2012-05-31'}, {'2012-06-01'}, {'2012-06-29'}, {'2012-09-03'}, {'2013-03-12'}, {'2013-08-19'},
          {'2014-09-01'}, {'2015-04-10'}, {'2015-04-16'}, {'2015-07-08'}, {'2015-08-03'}...
    , {'2015-08-26'}, {'2015-08-27'}, {'2015-08-28'}, {'2015-08-31'}, {'2015-09-07'}, {'2016-01-08'}, {'2017-02-17'}]
';
elseif
strcmp(IndexLabel, 'IH')
Index = '000016.SH';
SheetName = '上证50';
% StartDate = '2015-04-16';
time_p = [{'2015-07-08'}, {'2015-08-03'}, {'2015-08-26'}, {'2015-08-27'}, {'2015-08-28'}, {'2015-08-31'},
          {'2015-09-07'}, {'2016-01-08'}, {'2017-02-17'}]
';

else
return

end
StartYear = str2num(StartDate(1:4)); % 数字转换成字符串，以这种方式来截取年，月，日
StartMonth = str2num(StartDate(6:7));
EndYear = str2num(EndDate(1:4));
EndMonth = str2num(EndDate(6:7));
lengthofmonth = 12 * (EndYear - StartYear) + EndMonth - StartMonth; % 计算一共有多少个月份

[VOLUME, ~, ~, TradeDate, ~, ~] = w.wsd(Future0, 'volume', StartDate, EndDate, 'Fill=Previous');
[VOLUME1, ~, ~, TradeDate, ~, ~] = w.wsd(Future1, 'volume', StartDate, EndDate, 'Fill=Previous');
[VOLUME2, ~, ~, TradeDate, ~, ~] = w.wsd(Future2, 'volume', StartDate, EndDate, 'Fill=Previous');
[VOLUME3, ~, ~, TradeDate, ~, ~] = w.wsd(Future3, 'volume', StartDate, EndDate, 'Fill=Previous');
[VOLUME4, ~, ~, TradeDate, ~, ~] = w.wsd(Future4, 'volume', StartDate, EndDate, 'Fill=Previous');

TradeDate = datestr(TradeDate, 'yyyy-mm-dd');

Policy = ones(size(TradeDate, 1), 1) * nan; % policy是当天的结算价减去收盘价


Fdata_weight1 = zeros(length(TradeDate), 1);
Fdata_weight2 = zeros(length(TradeDate), 1);
indexnum = zeros(length(TradeDate), 1);

indexnum = w.wsd(Index, 'close', StartDate, EndDate, 'Fill=Previous');
Fdata_00 = w.wsd(Future0, 'settle', StartDate, EndDate, 'Fill=Previous'); % settle是股指期货的结算价
Fdata_01 = w.wsd(Future1, 'settle', StartDate, EndDate, 'Fill=Previous');
Fdata_02 = w.wsd(Future2, 'settle', StartDate, EndDate, 'Fill=Previous');
Fdata_03 = w.wsd(Future3, 'settle', StartDate, EndDate, 'Fill=Previous');
Fdata_04 = w.wsd(Future4, 'settle', StartDate, EndDate, 'Fill=Previous');

BaseDiff_00 = Fdata_00 - indexnum; % 此处不是基差，而是当天的结算价减去收盘价
BaseDiff_01 = Fdata_01 - indexnum; % 此处才是基差
BaseDiff_02 = Fdata_02 - indexnum;
BaseDiff_03 = Fdata_03 - indexnum;
BaseDiff_04 = Fdata_04 - indexnum;

average_basediff = mean([BaseDiff_01, BaseDiff_02, BaseDiff_03, BaseDiff_04], 2);
average_basediff1 = mean(
    [BaseDiff_01. * VOLUME1, BaseDiff_02. * VOLUME2, BaseDiff_03. * VOLUME3, BaseDiff_04. * VOLUME4], 2). / sum(
    [VOLUME1, VOLUME2, VOLUME3, VOLUME4], 2); % 加权值

DateStr = [];
n = 1;
for i=1: size(TradeDate, 1)
TempStr = {TradeDate(i,:)};
DateStr = [DateStr;
{TradeDate(i,:)}];
if n <= length(time_p)
    if strcmp(TempStr, time_p(n))
        Policy(i) = BaseDiff_00(i);
    n = n + 1;
    end
end
end
% %
Title = {'日期', strcat(Future0, '基差'), strcat(Future1, '基差'), strcat(Future2, '基差'), strcat(Future3, '基差'),
         strcat(Future4, '基差'), ...
         strcat(Future0, '成交量'), strcat(Future1, '成交量'), strcat(Future2, '成交量'), strcat(Future3, '成交量'),
         strcat(Future4, '成交量'), SheetName, '平均基差指数', '加权平均指数', '政策'};
data = [DateStr, num2cell(BaseDiff_00), num2cell(BaseDiff_01), num2cell(BaseDiff_02), num2cell(BaseDiff_03),
        num2cell(BaseDiff_04), num2cell(VOLUME), num2cell(VOLUME1), num2cell(VOLUME2), num2cell(VOLUME3),
        num2cell(VOLUME4), num2cell(indexnum), num2cell(average_basediff), num2cell(average_basediff1),
        num2cell(Policy)];
Tdata = [Title;
data];

XLSName = strcat('V1长期基差成本分析从', StartDate, '到', EndDate, '.xlsx');
[status, message] = xlswrite(XLSName, Tdata, SheetName, 'A1');
% system('tskill excel')
